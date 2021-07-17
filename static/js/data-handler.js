$(document).ready(function(){
       $('#refresh').click(function () {
              
        $.ajax({
            url: '/saved_data',
            dataType: "json",
            contentType: "application/json",
            
            type: 'GET',
            success: function (response) {
                res = response;
                data = res["data"]
                console.log(data);
                if (res["status"] === "working") {
                    var eachrow = "<tr>" + "<td>" + "<p class='name'>" +"saved data: " +data + "</p>" + "</td>" + "</tr>";
                    
                    

                        $("#tbody").append(eachrow);
                } else {
                    alert("not working");

                }

            },
            error: function (error) {
                alert("No data found")
                console.log(error);
            }
        });
       });
        
       });
