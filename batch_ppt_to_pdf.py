import win32com.client
import os

def init_powerpoint():
    powerpoint = win32com.client.DispatchEx("Powerpoint.Application")
    return powerpoint

def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType = 32):
    if outputFileName[-3:] != 'pdf':
        outputFileName = os.path.splitext(outputFileName)[0] + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()

def convert_files_in_folder(powerpoint, folder):
    files = os.listdir(folder)
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    for pptfile in pptfiles:
        fullpath = os.path.join(folder, pptfile)
        ppt_to_pdf(powerpoint, fullpath, fullpath)

if __name__ == "__main__":
    powerpoint = init_powerpoint()
    cwd = os.getcwd()
    convert_files_in_folder(powerpoint, cwd)
    powerpoint.Quit()
