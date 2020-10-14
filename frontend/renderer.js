// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
document.onkeydown = function(e) {
  switch(e.which) {
      case 37: // left
      console.log("left pressed");
      break;

      case 38: // up
      console.log("up pressed");
      break;

      case 39: // right
      console.log("right pressed");
      break;

      case 40: // down
      console.log("down pressed");
      break;

      default: return; // exit this handler for other keys
  }
  e.preventDefault(); // prevent the default action (scroll / move caret)
};
