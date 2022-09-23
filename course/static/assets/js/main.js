const courseLogoUpload = document.querySelector("#id_course_logo");
const courseLogoImg = document.querySelector("#id_logo_img");
const courseProfileUpload = document.querySelector("#id_course_profile");
const courseProfileImg = document.querySelector("#id_profile_img");
const eventImgUpload = document.querySelector("#id_photo");
const eventImg = document.querySelector("#id_event_img");

const onChangeImage = (input, img) => {
  if (input && img) {
    input.addEventListener("change", () => {
      const [file] = input.files;
      if (file) {
        img.src = URL.createObjectURL(file);
      }
    });
  }
};

onChangeImage(courseLogoUpload, courseLogoImg);
onChangeImage(courseProfileUpload, courseProfileImg);
onChangeImage(eventImgUpload, eventImg);
