function setup() {
  createCanvas(700, 700);
  background(0);
  let submitButton = document.getElementById("submit");
  let clearButton = document.getElementById("clear");
  submitButton.onclick = () => {
    fetchData();
  };
  clearButton.onclick = () => {
    background(0);
  };
}

const fetchData = async () => {
  let canvas = document.getElementById("defaultCanvas0");
  let dataUrl = canvas.toDataURL();
  const response = await $.ajax({
    url: "/submit",
    type: "POST",
    dataType: "json",
    data: JSON.stringify({ base64: dataUrl }),
    contentType: "application/json",
  });
  let labelText = document.getElementById("label-text");
  labelText.innerHTML = `Is it: ${response["label"]}`;
};

function draw() {
  if (mouseIsPressed) {
    stroke(255);
    strokeWeight(20);
    line(mouseX, mouseY, pmouseX, pmouseY);
  }
}
