text = "X-DSPAM-Confidence:    0.8475";


strtPos = text.find(' ')
endPos = len(text) 
 
while strtPos != -1:
	strtPos = text.find(' ',strtPos+1)
    
	if strtPos != -1:
		newStrtPos = strtPos


print text[newStrtPos+1:endPos]