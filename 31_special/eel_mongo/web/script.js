

$(function () {


  $("body").on("click", "#save-customer", () => {
    $.confirm({
      title: 'What is up?',
      content: 'Here goes a little content',
      type: 'green',
      buttons: {
        ok: {
          text: "ok!",
          btnClass: 'btn-primary',
          keys: ['enter'],
          action: function () {
            console.log('the user clicked confirm');
            var data =  $("#customer-form").serialize();
            console.log(data);
            eel.saveCustomer(data)((response) => {
              $('#customer-id').html("Customer ID: "+response);
            });
          }
        },
        cancel: function () {
          console.log('the user clicked cancel');
        }
      }
    });
  });

  $("body").on("click", "#show-students", () => {
    eel.showStudents()((response) => {
      console.log(response)
    });
  });



  $("body").on("click", "#add", () => {
    let num1 = $("#number1").val();
    let num2 = $("#number2").val();
    eel.sum(num1, num2)((number) => {
      $("#answer").val(number);
    });
  });

  $("body").on("click", "#sub", () => {
    let num1 = $("#number1").val();
    let num2 = $("#number2").val();
    eel.sub(num1, num2)((number) => {
      $("#answer").val(number);
      $("#answerHelp").html("Answer for Subtraction");
    });
  });

  $("body").on("click", "#mul", () => {
    let num1 = $("#number1").val();
    let num2 = $("#number2").val();
    eel.mul(num1, num2)((number) => {
      $("#answer").val(number);
      $("#answerHelp").html("Answer for Multipication");
    });
  });

  $("body").on("click", "#div", () => {
    let num1 = $("#number1").val();
    let num2 = $("#number2").val();
    eel.div(num1, num2)((number) => {
      $("#answer").val(number);
      $("#answerHelp").html("Answer for Division");
    });
  });

  $("body").on("click", "#mod", () => {



    let num1 = $("#number1").val();
    let num2 = $("#number2").val();
    eel.mod(num1, num2)((number) => {
      $("#answer").val(number);
      $("#answerHelp").html("Answer for Modulus");
    });
  });
});