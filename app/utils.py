from fpdf import FPDF

def generate_pdf(name:str, email:str, points: int, feedbacks: list):
    pdf = FPDF() 
    pdf.add_page() 
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = f"<Hack-Dev/>",  
            ln = 1, align = 'C', )

    pdf.cell(200, 10, txt = "",  
            ln = 1, align = 'C', )

    pdf.cell(200, 10, txt = f"Nome: {name}",  
            ln = 1, align = 'L') 
    pdf.cell(200, 10, txt = f"Pontos: {points}", 
            ln = 2, align = 'L') 
    pdf.cell(200, 10, txt = f"Email: {email}", 
            ln = 2, align = 'L') 
    pdf.cell(200, 10, txt = f"Total de feedbacks: {len(feedbacks)}", 
            ln = 2, align = 'L') 
    pdf.cell(200, 10, txt = "Feedbacks:", 
            ln = 2, align = 'L') 

    for index in range(0, len(feedbacks)):
        pdf.multi_cell(180, 7, f"feedback - {index+1}: {feedbacks[index]}\n\n")
    #return pdf
    pdf.output(f"/tmp/{name.split(' ')[0]}.pdf")