from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from users.utils import log_actiune
from core.models import Ferma, Fabrica, ProductieFerma, ProductieFabrica, TestCalitateFabrica, TestCalitateFerma
from django.utils.dateparse import parse_date
import csv
import io
import openpyxl
from openpyxl.utils import get_column_letter

@login_required
def raport_view(request):
    if not (request.user.is_superuser or request.user.face_rapoarte or request.user.rol == 'admin'):
        raise PermissionDenied("Nu ai permisiunea să creezi rapoarte.")

    if request.method == "POST":
        tip = request.POST['tip_raport']
        data_start = request.POST.get('data_start')
        data_end = request.POST.get('data_end')
        format_fisier = request.POST['format']

        data_start = parse_date(data_start) if data_start else None
        data_end = parse_date(data_end) if data_end else None

        model_map = {
            'ferme': Ferma,
            'fabrici': Fabrica,
            'productie_ferme': ProductieFerma,
            'productie_fabrici': ProductieFabrica,
            'teste_ferme': TestCalitateFerma,
            'teste_fabrici': TestCalitateFabrica,
        }

        model = model_map.get(tip)
        if not model:
            return HttpResponse("Tip raport invalid", status=400)

        queryset = model.objects.all()

        # Filtrare dupa date de adaugare
        date_fields = [f.name for f in model._meta.fields if
                       'data' in f.name.lower() and f.get_internal_type() in ['DateField', 'DateTimeField']]
        if date_fields and data_start and data_end:
            date_field = date_fields[0]
            queryset = queryset.filter(**{f"{date_field}__range": [data_start, data_end]})

        # Extrage datele sub formă de listă de dict-uri
        rows = list(queryset.values())
        if not rows:
            return HttpResponse("Nicio înregistrare găsită.", status=204)

        # Extrage header
        header = rows[0].keys()

        # === FORMAT CSV ===
        if format_fisier == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{tip}_raport.csv"'

            writer = csv.DictWriter(response, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)
            return response

        # === FORMAT EXCEL (.xlsx) ===
        elif format_fisier == 'xlsx':
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Raport"

            # Header
            for col_num, column_title in enumerate(header, 1):
                col_letter = get_column_letter(col_num)
                ws[f'{col_letter}1'] = column_title

            # Content
            for row_num, row in enumerate(rows, 2):
                for col_num, column_title in enumerate(header, 1):
                    ws.cell(row=row_num, column=col_num, value=row[column_title])

            # workbook-ul în buffer
            output = io.BytesIO()
            wb.save(output)
            output.seek(0)

            #  raspunsul cu bufferul
            response = HttpResponse(
                output.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename="{tip}_raport.xlsx"'
            return response

        # === FORMAT PDF ===
        elif format_fisier == 'pdf':
            try:
                from weasyprint import HTML
            except ImportError:
                return HttpResponse("WeasyPrint nu este instalat. Folosește CSV sau Excel.", status=500)

            table_html = "<table border='1'><thead><tr>" + "".join(
                [f"<th>{col}</th>" for col in header]) + "</tr></thead><tbody>"
            for row in rows:
                table_html += "<tr>" + "".join([f"<td>{row[col]}</td>" for col in header]) + "</tr>"
            table_html += "</tbody></table>"

            html_content = f"<html><body><h2>Raport: {tip.replace('_', ' ').title()}</h2>{table_html}</body></html>"
            pdf_file = HTML(string=html_content).write_pdf()

            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{tip}_raport.pdf"'
            return response

        else:
            return HttpResponse("Format de fișier invalid.", status=400)

    user = request.user
    log_actiune(request.user, f"{user.username} a creat un raport.")
    return render(request, 'core/creare_raport.html')