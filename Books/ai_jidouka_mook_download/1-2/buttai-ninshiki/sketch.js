let classifier;
let video;
let label = "";

function setup() {
    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    classifier = ml5.imageClassifier("MobileNet", video, modelLoaded);
}

function draw() {
    image(video, 0, 0);
    fill(255);
    textSize(32);
    text(label, 10, height - 10);
}

function modelLoaded() {
    console.log("Model Loaded!");
    classifier.predict(gotResults);
}

function gotResults(err, results) {
    if (err) {
        console.error(err);
    } else {
        console.log(results);
        label = results[0].className;
        classifier.predict(gotResults);
    }
}