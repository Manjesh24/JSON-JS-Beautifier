# JSON/Javascript Beautifier
# Author: Manjesh S (@Manjesh24)

from burp import IBurpExtender               
from burp import IMessageEditorTab           
from burp import IMessageEditorTabFactory    
import jsbeautifier



ContentTypes = [
    "application/json",
    "text/json",
    "text/x-json",
    "application/javascript",
    "text/javascript",
]

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):

    def registerExtenderCallbacks(self, callbacks):

        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("JSON/JS Beautifier")
        callbacks.registerMessageEditorTabFactory(self)
        print("---Beautifier Installed---")
        return
        
    def createNewInstance(self, controller, editable):
        return DisplayValues(self, controller, editable)


class DisplayValues(IMessageEditorTab):
    def __init__(self, extender, controller, editable):
        self._txtInput = extender._callbacks.createTextEditor()
        self._extender = extender

    def getUiComponent(self):
        return self._txtInput.getComponent()
    
    def getTabCaption(self):
        return "JSON/JS Beautifier"
        
    def isEnabled(self, content, isRequest):
        if isRequest == True:
            re = self._extender._helpers.analyzeRequest(content)
        else:
            re = self._extender._helpers.analyzeResponse(content)
            
        for header in re.getHeaders():
          if header.lower().startswith("content-type:"):
            content_type = header.split(":")[1].lower()

            for allowedType in ContentTypes:
              if content_type.find(allowedType) > 0:
                extdata = content[re.getBodyOffset():].tostring()
                try:
                        self._decodedAuthorizationHeader = jsbeautifier.beautify(extdata)
                except Exception as e:
                        print(e)
                        self._decodedAuthorizationHeader = "Unable to beatify. Please check extender logs."
                return True    
        return False
        
    def setMessage(self, content, isRequest):
        if (content is None):
            self._txtInput.setText(None)
            self._txtInput.setEditable(False)
        else:
            self._txtInput.setText(self._decodedAuthorizationHeader)
        return
   