
	var tier = document.getElementsByName('tier')
	var img = document.createElement('img')
	img.setAttribute('id', 'foto')

	var tier = tier[0]

	img.setAttribute('src', '{% static 'lol/assets/Emblem_Gold.png' %}')

	tier.appendChild(img)