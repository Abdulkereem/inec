from django.test import TestCase

# Create your tests here.

import weasyprint

pdf = weasyprint.HTML('http://localhost:8000').write_pdf('./test.pdf')
