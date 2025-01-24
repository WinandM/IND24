// Récupérer les liens du menu
const links = document.querySelectorAll('nav a');
const iframe = document.getElementById('content-frame');

// Ajouter un événement pour chaque lien
links.forEach(link => {
    link.addEventListener('click', (e) => {
        // Empêcher le comportement par défaut du lien (rechargement de la page)
        e.preventDefault();

        // Récupérer la valeur de l'attribut `data-page` du lien cliqué
        const page = link.getAttribute('data-page');

        // Mettre à jour la source de l'iframe pour afficher la nouvelle page
        iframe.src = `pages/${page}`;

        // Mettre à jour la classe active sur le lien cliqué
        links.forEach(l => l.classList.remove('active')); // Retirer la classe active de tous les liens
        link.classList.add('active'); // Ajouter la classe active au lien actuel
    });
});
