import urllib, os, xbmc, xbmcgui
import base64
addon_id = 'plugin.video.live.pld'
data_folder = 'special://home/addons/plugin.video.live.pld/'
Url = base64.b64decode('aHR0cDovL3Byb3llY3RvbHV6ZGlnaXRhbC5pbmZvL3R2Z3VpYS9kb3dubG9hZC9hY3RpcGxheWVyLzEv')
File = ['source_file']

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("ACTIVANDO PLAYER.PROYECTOLUZDIGITAL","Introduciendo Codigo",' ', ' ')
    dp.update(0)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url, dp):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Cancelar")
        dp.close()

for file in File:
	url = Url + file
	fix = xbmc.translatePath(os.path.join( data_folder, file))
	download(url, fix)
	
import urllib, os, xbmc, xbmcgui
import base64
	
addon_id = 'plugin.video.live.pld'
data_folder = 'special://userdata/addon_data/' + addon_id
Url = base64.b64decode('aHR0cDovL3Byb3llY3RvbHV6ZGlnaXRhbC5pbmZvL3R2Z3VpYS9kb3dubG9hZC9hY3RpcGxheWVyLzEv')
File = ['settings.xml']

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("ACTIVANDO TVGUIA-PLD","Introduciendo Codigo",' ', ' ')
    dp.update(0)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url, dp):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Cancelar")
        dp.close()

for file in File:
	url = Url + file
	fix = xbmc.translatePath(os.path.join( data_folder, file))
	download(url, fix)	
	
	
	
	
d = xbmcgui.Dialog()
d.ok('ACTIVADOR PLAYER.PROYECTOLUZDIGITAL', '        [COLOR red]                     El PLAYER.PROYECTOLUZDIGITAL ha sido Acivado                   [/COLOR]', '          ya puedes usar el[COLOR blue] PLAYER.PROYECTOLUZDIGITAL [/COLOR]', '[COLOR red]   Os Deseamos FELICES FIESTAS                   [/COLOR]')  