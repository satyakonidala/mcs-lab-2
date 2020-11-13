// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
flaskServerUrl = "http://localhost:5000/post-to-car"

const sendAjaxRequest = function (data) {
  console.log("sending data: ", data)
  $.post( flaskServerUrl, { data: data } , function(data, status){
    car_info = JSON.parse(data)
    $("#cpu_temperature").text(car_info.cpu_temperature +"C")
    $("#cpu_usage").text(car_info.cpu_usage + "%")
    $("#battery").text(car_info.battery + "W")
  });
}

$(document).ready ( function(){
  sendAjaxRequest('dummy');
})

document.onkeydown = function(e) {
  switch(e.which) {
      case 37: // left
      sendAjaxRequest("left")
      break;

      case 38: // forward
      sendAjaxRequest("forward")
      break;

      case 39: // right
      sendAjaxRequest("right")
      break;

      case 40: // back
      sendAjaxRequest("back")
      break;

      default: return; // exit this handler for other keys
  }
  e.preventDefault(); // prevent the default action (scroll / move caret)
};
