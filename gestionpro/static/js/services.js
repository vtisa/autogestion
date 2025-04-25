  // Función simple para mostrar/ocultar el modal
  function toggleModal(element) {
    // Encuentra la tarjeta padre
    const card = element.closest('.service-card');
    
    // Encuentra el modal dentro de la tarjeta
    const modal = card.querySelector('.modal-popup');
    
    // Cambia la visibilidad del modal
    if (modal.style.display === 'block') {
        modal.style.display = 'none';
    } else {
        modal.style.display = 'block';
    }
}

