// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
flaskServerUrl = "http://localhost:5000/post-to-car"
document.onkeydown = function(e) {
  switch(e.which) {
      case 37: // left
      console.log("left pressed");
      $.post( flaskServerUrl, { data: "left" } );
      break;

      case 38: // up
      console.log("forward pressed");
      $.post( flaskServerUrl, { data: "forward" } );
      break;

      case 39: // right
      console.log("right pressed");
      $.post( flaskServerUrl, { data: "right" } );
      break;
      down
      case 40: // down
      console.log("back pressed");
      $.post( flaskServerUrl, { data: "back" } );
      break;

      default: return; // exit this handler for other keys
  }
  e.preventDefault(); // prevent the default action (scroll / move caret)
};
