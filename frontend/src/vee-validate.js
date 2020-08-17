import { required, confirmed, email, max, min } from "vee-validate/dist/rules";
import { extend } from "vee-validate";

extend("required", {
  ...required,
  message: "This field is required",
});

extend("email", {
  ...email,
  message: "Enter valid email",
});

extend("confirmed", {
  ...confirmed,
  message: "Password and Confirm Password field do not match",
});

extend("max", {
  ...max,
  message: "Max {length} characters allowed",
});

extend("min", {
  ...min,
  message: "Min {length} characters required",
});
