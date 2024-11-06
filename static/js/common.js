const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
$.ajaxSetup({
    headers: { "X-CSRFToken": csrftoken }
});

$(document).ready(function() {
    $('.toast').each(function() {
        const toast = new bootstrap.Toast(this, { delay: 10000 });
        toast.show();
    });
});

function formatLabel(key) {
    // Replace underscores with spaces and capitalize the first letter of each word
    return key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}