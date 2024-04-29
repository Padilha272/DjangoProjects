from django.http import HttpResponse 
from django.views.generic import TemplateView

class VarietyHtml(TemplateView):
    def get(self, request):
        if request.method == 'GET':
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Variety App</title>
            </head>
            <body>
                <h1>Welcome to Variety App!</h1>
                <p>This is a sample HTML view in the Variety App.</p>
            </body>
            </html>
            """
            return HttpResponse(html_content)
        else:
            # Handle other HTTP methods (e.g., POST, PUT, DELETE)
            return HttpResponse(status=405)  # Method Not Allowed
