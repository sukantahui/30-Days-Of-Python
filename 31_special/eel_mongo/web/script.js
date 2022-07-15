

$(function () {


  $("body").on("click", "#save-customer", () => {
    $.confirm({
      title: 'Save Customer',
      content: 'Do you want to save?',
      type: 'green',
      buttons: {
        ok: {
          text: "ok!",
          btnClass: 'btn-primary',
          keys: ['enter'],
          action: function () {
            console.log('the user clicked confirm');
            let form = document.querySelector('#customer-form');

            // Get all field data from the form
            // returns a FormData object
            let data = new FormData(form);
            let qryString="";
            for (let [key, value] of data) {
              if(qryString.length>0){
                qryString+="&";
              }
              qryString=qryString+key+"="+value;
            }
            console.log(qryString);
            // var data =  $("#customer-form").serialize();
            eel.saveCustomer(qryString)((response) => {
              $('#customer-id').html("Customer ID: "+response.current_id);
              $('#customer-table-div').html(response.return_html);
            });
          }
        },
        cancel: function () {
          console.log('the user clicked cancel');
        }
      }
    });
  });

  $("#customer-table-div").on("click", ".select-cutomer", (event) => {
    console.log(event);
    // event.preventDefault();
    // event.stopPropagation();
    var d=$(event.currentTarget).attr('cust-id');
    // var d = $(self).attr('data-value');      
    alert(d);
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