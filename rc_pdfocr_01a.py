import fitz
from PIL import Image
import pytesseract
import cv2
import re
import glob
from pathlib import Path
import os
import pandas as pd
import numpy as np




class getText:
    
    def __init__(self):
        
        #global variables
        
        self.town_list = []
        self.town_dict = {}
        self.pdf_glob = glob.glob('*.pdf')
        
    def ocr_text(self, page, pno):
        getimg = page.get_pixmap()
        saveimg = getimg.save('curpage.png')
        rdyimg = cv2.imread('curpage.png')
        return self.preprocess(rdyimg)
    
        
    def preprocess(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply dilation and erosion to remove some noise
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        
        #  Apply threshold to get image with only black and white
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        result = pytesseract.image_to_string(img, lang="eng")
        
        return result
        
    def img_or_text(self, page):
        
        ptext = page.get_text('text',sort=True)
        if len(str(' '.join(ptext).split())) < 10:
            return 'img'
        else:
            if 'ownship' or 'rdinance' or 'arijuana'  in ptext:
                return 'txt'
            else:
                return 'wrong'
    
    def get_page_text(self, page, pno):
        
        wtype = self.img_or_text(page)
        if wtype == 'img':
            ocrp = self.ocr_text(page, pno)
            
            return ocrp
        else:
        
            ptext = ''
            
            try:
                t = page.get_text('text', sort=True)
            except Exception:
                t = 'error'
            
            ptext +=t
            return ptext
    
    def get_pdf_text(self, pdffile):
        try:
            pf = fitz.open(pdffile)
        except:
            pf = ''
        
        if pf == '':
            return False
        
        town = str(pf).split('_')[0]
        nop = pf.page_count
        i = 0
        pages_text = []
        page_text = []
        for p in range(nop):
            cpage = pf.load_page(i)
            ctext = self.get_page_text(cpage, i)
            page_text.append({'page':i, 'text':ctext})
            i+=1
        pages_text.append({'town':town, 'text':page_text})
        return pages_text
    
    def process_pdfs(self,pdfglob):
        pdfs_text = []
        for pdf in self.pdf_glob:
            curpdf = self.get_pdf_text(pdf)
            if curpdf == False:
                continue
            pdfs_text.append(curpdf)
        return pdfs_text
            
    
            
                
                
            
            
    
        
    #code
