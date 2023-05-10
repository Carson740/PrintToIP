#test.py

import pip._vendor.requests as requests
import traceback

def checkValid(printType, printerIP):
    url = "http://" + printerIP
    try:
        r = requests.get(url)

        if any(x in r.text for x in genericPrinters):
            isValid = "WrongType"
            print("Working: ", isValid)
        elif 'genericPrinters' in r.text and printType in labelList:
            isValid = "WrongType"
        else:
            isValid = True
            print("Working: ", isValid)
        return isValid
    except Exception:
        isValid = "NoConnect"
        print(traceback.format_exc())
        return isValid
    

labelList = ["print_label_4x6"]
labelPrinters = ["ZD621", "Printronix"]

genericList = ["print_pdf_b&w", "print_pdf_color"]
genericPrinters = ["Kyocera", "Ricoh"]

print(checkValid("print_pdf_b&w", "DVAS9B16T01"))
