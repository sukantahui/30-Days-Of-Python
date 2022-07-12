
  
  $(function() {

    eel.fetch_tag()(function(response){
      $('#tag').val(response.tag_number);
      $('#tag-prefix').val(response.tag_prefix);
    });
    
    $("body").on("click", "#generate-random", ()=> {
      eel.random_python()((number)=>{
        $('.random_number').text(number);
      });
    });

    $("body").on("click", "#update-ip", ()=> {
      var ip=$('#ip-address').val();
      eel.update_ip(ip)((number)=>{
        
      });
    });

    // $('#generate-random').click(function(){
    //     eel.random_python()(function(number){
    //       $('.random_number').text(number);
    //     });
    // });

    $("#add-numbers").click(function() {
      var data_1 = $("#int1").val();  
      var data_2 = $("#int2").val();  
      eel.add(data_1, data_2)(function(output){
          $('#res').val(output);
      })
    });

    $("body").on("click", "#fetch-request", ()=> {
      var jobId=$('#input-job-id').val();
      eel.fetchTagDetails(jobId)(function(requestData){
        var jsonobj = requestData;
        console.log(jsonobj);
        $("#job-id").val(jsonobj.job_id);
        $("#order-id").val(jsonobj.order_id);
        $("#product-code").val(jsonobj.product_code);
        $("#product-size").val(jsonobj.product_size);

        $("#price-code").val(jsonobj.price_code);
        $("#price").val(jsonobj.price);
        $("#pieces").val(jsonobj.pieces);
        $("#status").val(jsonobj.status_name);
        $("#cust-name").val(jsonobj.cust_name);
        $("#cust-short-name").val(jsonobj.short_name);
        $("#total-lc").val(jsonobj.total_lc);
        $("#gold-used").val(jsonobj.gold_used);
        $("#product-wt").val(jsonobj.product_wt);
          // $('#request-output').text(jsonobj.order_id);
      })
    });

    $("body").on("click", "#print-tag", ()=> {
      // var data = $("#tag-form").json();  
      var data =  $("#tag-form").serialize();
      console.log(data);
      eel.printTag(data)(function(){

        });
    });
    
    // $("#fetch-request").click(function() { 
    //   eel.fetchTagDetails('JOB-00001-2122')(function(requestData){
    //     var jsonobj = requestData;
    //     console.log(jsonobj);
    //     $("#job-id").val(jsonobj.job_id);
    //     $("#order-id").val(jsonobj.order_id);
    //     $("#product-code").val(jsonobj.product_code);
    //     $("#product-size").val(jsonobj.product_size);
    //       // $('#request-output').text(jsonobj.order_id);
    //   })
    // });

    $("#test-bat").click(function() { 
      eel.runBatch()(function(){
       console.log('running batch');
      })
    });

    // readymade codes
    $("body").on("change", "#price-code", ()=> {
      // var data = $("#tag-form").json();  
      console.log();
      var data=$('#price-code').val();
      console.log(data);
      eel.get_price_ploss(data)((response)=>{
        $("#ploss").val(response.ploss);
        $("#lc").val(response.price);
        $("#total-ploss").val(response.ploss * parseInt($("#pieces").val()));
        $("#total-lc").val(response.price * parseInt($("#pieces").val()));
      });
    });

    $("body").on("change", "#pieces", ()=> {
      $("#total-ploss").val(parseFloat($("#ploss").val()) * parseInt($("#pieces").val()));
      $("#total-lc").val(parseInt($("#lc").val()) * parseInt($("#pieces").val()));
    });

    $("body").on("click", "#new-tag", ()=> {
      tag_number = parseInt($("#tag").val())
      eel.new_tag(tag_number)((response)=>{
        $("#tag").val(response.tag_number)
        $('#product-code').val("")
        $('#pieces').val("")
        $('#gold-used').val("")
        $('#fine-gold').val("")
        $('#gross-weight').val("")
        $('#size').val("")
        $('#total-lc').val("")
      });
    });

    $("body").on("change", "#gold-used", ()=> {
      fineGold = parseFloat((parseFloat($("#gold-used").val()) * 92.0/100)).toFixed(3);
      $("#fine-gold").val(fineGold)
    });

    $("body").on("click", "#next-tag", ()=> {
      tag_number = parseInt($("#tag").val())
      eel.increase_tag(tag_number)((response)=>{
        $("#tag").val(response.tag_number)
      });
    });
});