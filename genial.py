import PyPDF2

def parse(file):
    pdf_reader = PyPDF2.PdfReader(file)

    for page in pdf_reader.pages:
        print("\n".join(parsePage(page.extract_text())))

def parsePage(text):
    lines = text.split("\n")
    i = 0
    ix = 0
    parsed = []

    for line in lines:
        i += 1

        if ix > 0 or line == "Resumo dos Negócios Resumo Financeiro D/C":
            ix += 1

        if i == 3:
            parsed.append(line)

        if i >= 22 and ix == 0:
            parsed.append(line)

        if ix > 3 and ix < 30:
            parsed.append(line)

    return parsed
