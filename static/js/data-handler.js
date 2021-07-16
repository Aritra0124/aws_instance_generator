$(document).ready(function(){
       $('#s3_create').click(function () {
        var location = $("#regions").val();
        

        $.ajax({
            url: '/s3',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({
                
                location: location
            }),
            type: 'POST',
            success: function (response) {
                res = response;
                data = res["response"]
                console.log(data["ResponseMetadata"]);
                if (res["status"] === "working") {
                    var eachrow = "<tr>" + "<td>" + "<p class='name'>" +"S3 Instance: " +data + "</p>" + "</td>" + "</tr>";
                    
                    

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
