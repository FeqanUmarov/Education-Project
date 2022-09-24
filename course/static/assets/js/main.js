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

// accordion
const openIcon1 = document.getElementById("accordion-open1");
const accordionBtn1 = document.querySelector("#accordion-button1");
const openIcon2 = document.getElementById("accordion-open2");
const accordionBtn2 = document.querySelector("#accordion-button2");

accordionBtn1.addEventListener("click", () => {
  openIcon1.classList.toggle("show-accordion");
});
accordionBtn2.addEventListener("click", () => {
  openIcon2.classList.toggle("show-accordion");
  console.log(openIcon2);
});
