$(document).ready(function(){
       $('#s3_create').click(function () {
        var location = $("#regions").val();
        var aws_access_key_id = $("#acki").val();
        var aws_secret_access_key = $("#asak").val();
        var s3_name = $("#s3_name").val();
        var s3_acl = $("#acl").val();

        $.ajax({
            url: '/s3',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({
                s3_name: s3_name,
                s3_acl: s3_acl,
                aws_access_key_id: aws_access_key_id,
                aws_secret_access_key: aws_secret_access_key,
                location: location
            }),
            type: 'POST',
            success: function (response) {
                res = response;
                data = res["response"]
                console.log(data["ResponseMetadata"]);
                if (res["status"] === "working") {
                    var eachrow = "<tr>" + "<td>" + "<p class='name'>" +"S3 Instance: " +JSON.stringify(data["ResponseMetadata"]) + "</p>" + "</td>" + "</tr>";
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
        $('#ec2_create').click(function () {
            var location = $("#regions").val();
        var aws_access_key_id = $("#acki").val();
        var aws_secret_access_key = $("#asak").val();
        var ec2_image_id = $("#ec2_imageid").val();
        var ec2_instance = $("#instancetype").val();

        $.ajax({
            url: '/ec2',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({
                ec2_image_id: ec2_image_id,
                ec2_instance: ec2_instance,
                aws_access_key_id: aws_access_key_id,
                aws_secret_access_key: aws_secret_access_key,
                location: location
            }),
            type: 'POST',
            success: function (response) {
                res = response;

                if (res["status"] === "working") {
                    var eachrow = "<tr>" + "<td>" + "<p class='name'>" +"EC2 Instance ID: "+res["response"] + "</p>" + "</td>" + "</tr>";
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
         $('#rds_create').click(function () {
             var location = $("#regions").val();
        var aws_access_key_id = $("#acki").val();
        var aws_secret_access_key = $("#asak").val();
        var rds_instance_identifier = $("#db_instance_identifier").val();
        var rds_instance_class = $("#db_instance_class").val();
        var rds_db_name = $("#db_name").val();
        var rds_engine_name = $("#engine_name").val();
        var rds_master_username = $("#master_username").val();
        var rds_master_password = $("#master_password").val();
        var rds_storage_type = $("#storagetype").val();
        var rds_allocated_storage = parseInt($("#allocated_storage").val());
      $.ajax({
            url: '/rds',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({
                rds_allocated_storage:rds_allocated_storage,
                rds_db_name:rds_db_name,
                rds_engine_name:rds_engine_name,
                rds_instance_class:rds_instance_class,
                rds_instance_identifier:rds_instance_identifier,
                rds_master_username:rds_master_username,
                rds_master_password:rds_master_password,
                rds_storage_type:rds_storage_type,
                aws_access_key_id: aws_access_key_id,
                aws_secret_access_key: aws_secret_access_key,
                location: location
            }),
            type: 'POST',
            success: function (response) {
                res = response;
                data = res["response"];
                if (res["status"] === "working") {
                        var eachrow = "<tr>" + "<td>" + "<p class='name'>" +"RDS Instance: " +JSON.stringify(data) + "</p>" + "</td>" + "</tr>";
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
