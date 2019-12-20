function searchFunction() {
	var input = document.getElementById('searchBar');
	var filter = input.value.toLowerCase();
	var cards = document.getElementsByClassName('card');

	for (i = 0; i < cards.length; i++) {
		var title = cards[i].getElementsByTagName('h5')[0].innerText.toLowerCase();
		var content = cards[i].getElementsByTagName('p')[0].innerText.toLowerCase();
		if (title.indexOf(filter) > -1 || content.indexOf(filter) > -1)
			cards[i].style.display = "";
		else
			cards[i].style.display = "none";
	}
}
