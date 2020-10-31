//img upload preview (taken from stackoverflow)
function readURL(input) {
  console.log("triggered")
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#prv-img').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#img-upload").change(function() {
  readURL(this);
});