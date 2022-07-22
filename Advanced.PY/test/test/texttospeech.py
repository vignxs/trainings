from win32com.client import Dispatch

speak = Dispatch('SAPI.SpVoice').speak
speak('Hi Welcome to TERIFIC Python')