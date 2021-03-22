$(document).ready(function(){

   $('#inst').click(function (){
       if($('#inst').val()==="s3"){
            $('#s3_section').show();
            $('#ec2_section').hide();
            $('#rds_section').hide();
            $('#vpc_section').hide();
       }
       else if($('#inst').val()==="ec2"){
            $('#s3_section').hide();
            $('#ec2_section').show();
            $('#rds_section').hide();
            $('#vpc_section').hide();
       }
       else if($('#inst').val()==="rds"){
            $('#s3_section').hide();
            $('#ec2_section').hide();
            $('#rds_section').show();
            $('#vpc_section').hide();
       }
       else if($('#inst').val()==="vpc"){
            $('#s3_section').hide();
            $('#ec2_section').hide();
            $('#rds_section').hide();
            $('#vpc_section').show();
       }
   });
});