let get_responses = function() {
  let gender = document.querySelector('input[name = "gender"]:checked').value
  let race = document.querySelector('input[name = "race"]:checked').value
 	let age = $("input#age").val()
    return {'gender': gender.toString(),
      'race':race.toString(),
		  'age': parseInt(age)}
};
let send_responses_json = function(responses) {
    $.ajax({
        url: '/calculate',
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        success: function (data) {
            display_solutions(data);
        },
        data: JSON.stringify(responses)
    });
};
let display_solutions = function(solutions) {
    $("span#solution").html(solutions.predicted_recidivism + "and " + solutions.alt_life_recidivism)
    $("span#solutionb").html(solutions.alt_life_recidivism)
};

$(document).ready(function() {
    $("button#calculate").click(function() {
        let responses = get_responses()
        send_responses_json(responses);
    })
})