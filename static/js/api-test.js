$(document).ready(function(){
    $('#test-btn').click(function () {
        var test_data = $("#test").val();
     $.ajax({
         url: '/save_data',
         dataType: "json",
         contentType: "application/json",
         data: JSON.stringify({
            test_data: test_data
        }),
         type: 'POST',
         success: function (response) {
             res = response;
             data = res["data"]
             console.log(data);
             

         },
         error: function (error) {
             alert("No data found")
             console.log(error);
         }
     });
    });
     
    });
