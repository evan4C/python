// 各変数の初期化
let video;
let poseNet;
let poses = [];

let leftShoulderX = 0;
let leftShoulderY = 0;

let rightShoulderX = 0;
let rightShoulderY = 0;
let leftElbowX = 0;
let leftElbowY = 0;

let rightElbowX = 0;
let rightElbowY = 0;

let leftWristX = 0;
let leftWristY = 0;

let rightWristX = 0;
let rightWristY = 0;

let leftHipX = 0;
let leftHipY = 0;

let rightHipX = 0;
let rightHipY = 0;

let sound;
let guitar;

let previousRightHandY = 0;

let debug = false;

// 音声や画像ファイルの読み込み
function preload() {
        sound = loadSound("normal.m4a");
        sound2 = loadSound("bending.m4a");
        guitar = loadImage("guitar.png");
}

// ページを開いたときに一度だけ実行する処理
function setup() {
        createCanvas(640, 480);
        video = createCapture(VIDEO);
        video.hide();
        let poseNet = ml5.poseNet(video, modelLoaded);
        poseNet.on('pose', gotPoses);
        angleMode(DEGREES);

        checkbox = createCheckbox('Debug', false);
        checkbox.changed(toggleDebug);
        angleP = createP('Angle:');
}

// 定期的に繰り返し実行される処理
function draw() {
        image(video, 0, 0);

        let bodyX = (rightShoulderX + leftShoulderX + rightHipX + leftHipX) / 4;
        let bodyY = (rightShoulderY + leftShoulderY + rightHipY + leftHipY) / 4;

        let arm_ratio = 1.5
        let leftHandX = leftElbowX + (leftWristX - leftElbowX) * arm_ratio;
        let leftHandY = leftElbowY + (leftWristY - leftElbowY) * arm_ratio;

        let rightHandX = rightElbowX + (rightWristX - rightElbowX) * arm_ratio;
        let rightHandY = rightElbowY + (rightWristY - rightElbowY) * arm_ratio;

        let angle = atan2(leftHandY - bodyY, leftHandX - bodyX);

        // ギターの画像を表示
        const ratio = 2.5;
        let guitar_width = dist(rightShoulderX, rightShoulderY, leftShoulderX, leftShoulderY) * ratio;

        push();
        translate(bodyX, bodyY);
        const slide = 0.5
        translate((leftHandX - bodyX) * slide, (leftHandY - bodyY) * slide)
        rotate(angle);
        imageMode(CENTER);
        image(guitar, 0, 0, guitar_width, guitar.height * guitar_width / guitar.width);
        pop();

        // 右手の縦方向の速度が10以上ならギター音を鳴らす
        let v = rightHandY - previousRightHandY;
        previousRightHandY = rightHandY;
        const threshold = 10;
        const distance_threshold = 100;

        if (v > threshold && dist(bodyX, bodyY, rightWristX, rightHandY) < distance_threshold) {
                sound.play();
        }

        // ギターを立てたときにギター音を変える
        const bending_angle = -30

        if (angle < bending_angle && sound.isPlaying() && !sound2.isPlaying()) {
                sound.stop()
                sound2.play();
        }

        // デバッグ用
        if (debug) {

                // キーポイントやスケルトンの表示
                drawKeypoints();
                drawSkeleton();

                // 角度の表示
                if (angle < bending_angle) {
                        angleP.style("color", "red");
                } else {
                        angleP.style("color", "black");
                }
                angleP.html(`Angle: ${round(angle)}`)

                // 右手、左手の予測位置に青丸を表示し、青い線で手首をつなげる
                strokeWeight(4);
                stroke(0, 0, 255);
                line(leftWristX, leftWristY, leftHandX, leftHandY);
                line(rightWristX, rightWristY, rightHandX, rightHandY);
                fill(0, 0, 255);
                noStroke();
                ellipse(leftHandX, leftHandY, 10, 10);
                ellipse(rightHandX, rightHandY, 10, 10);
        }
}

// PoseNetモデルの読み込みが完了したときに呼ばれるコールバック関数
function modelLoaded() {
        console.log('Model Loaded!');
}

// ポーズが変わるたびに呼ばれるコールバック関数
function gotPoses(results) {
        poses = results;
        if (poses.length > 0) {
                let newLeftShoulderX = poses[0].pose.leftShoulder.x;
                let newLeftShoulderY = poses[0].pose.leftShoulder.y;

                let newRightShoulderX = poses[0].pose.rightShoulder.x;
                let newRightShoulderY = poses[0].pose.rightShoulder.y;

                let newLeftElbowX = poses[0].pose.leftElbow.x;
                let newLeftElbowY = poses[0].pose.leftElbow.y;

                let newRightElbowX = poses[0].pose.rightElbow.x;
                let newRightElbowY = poses[0].pose.rightElbow.y;

                let newLeftWristX = poses[0].pose.leftWrist.x;
                let newLeftWristY = poses[0].pose.leftWrist.y;

                let newRightWristX = poses[0].pose.rightWrist.x;
                let newRightWristY = poses[0].pose.rightWrist.y;

                let newLeftHipX = poses[0].pose.leftHip.x;
                let newLeftHipY = poses[0].pose.leftHip.y;

                let newRightHipX = poses[0].pose.rightHip.x;
                let newRightHipY = poses[0].pose.rightHip.y;

                leftShoulderX = lerp(leftShoulderX, newLeftShoulderX, 0.25);
                leftShoulderY = lerp(leftShoulderY, newLeftShoulderY, 0.25);

                rightShoulderX = lerp(rightShoulderX, newRightShoulderX, 0.25);
                rightShoulderY = lerp(rightShoulderY, newRightShoulderY, 0.25);

                leftElbowX = lerp(leftElbowX, newLeftElbowX, 0.25);
                leftElbowY = lerp(leftElbowY, newLeftElbowY, 0.25);

                rightElbowX = lerp(rightElbowX, newRightElbowX, 0.25);
                rightElbowY = lerp(rightElbowY, newRightElbowY, 0.25);

                leftWristX = lerp(leftWristX, newLeftWristX, 0.25);
                leftWristY = lerp(leftWristY, newLeftWristY, 0.25);

                rightWristX = lerp(rightWristX, newRightWristX, 0.25);
                rightWristY = lerp(rightWristY, newRightWristY, 0.25);

                leftHipX = lerp(leftHipX, newLeftHipX, 0.25);
                leftHipY = lerp(leftHipY, newLeftHipY, 0.25);

                rightHipX = lerp(rightHipX, newRightHipX, 0.25);
                rightHipY = lerp(rightHipY, newRightHipY, 0.25);
        }
}

// デバッグモードON/OFFの切り替え
function toggleDebug() {
        if (this.checked()) {
                debug = true;
        } else {
                debug = false;
        }
}