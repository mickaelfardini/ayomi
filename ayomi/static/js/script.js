window.onload = function () {
	$("#updateEmail").submit((e) => {
		e.preventDefault();
		$.post("/", {
			email: $('#email').val(),
			firstname: $('#firstname').val(),
			lastname: $('#lastname').val(),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		})
		.done((data) => {
			if (data.type == 'success') {
				$('#uEmail').text(data.email);
				$('#uLastname').text(data.lastname);
				$('#uFirstname').text(data.firstname);
				$('#emailModal').modal('hide');
			}
		});
	});
};