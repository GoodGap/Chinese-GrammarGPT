<script setup>
import { computed } from "vue";
const props = defineProps({
  id: {
    type: String,
    default: "",
  },
  type: {
    type: String,
    default: "text",
  },
  label: {
    type: [String, Object],
    text: String,
    class: String,
    default: () => ({
      class: "",
    }),
  },
  value: {
    type: String,
    default: "",
  },
  modelValue: {
    type: String,
    default: "",
  },
  placeholder: {
    type: String,
    default: "",
  },
  size: {
    type: String,
    default: "md",
  },
  error: {
    type: Boolean,
    default: false,
  },
  success: {
    type: Boolean,
    default: false,
  },
  isRequired: {
    type: Boolean,
    default: false,
  },
  isDisabled: {
    type: Boolean,
    default: false,
  },
  inputClass: {
    type: String,
    default: "",
  },
  icon: {
    type: String,
    default: "",
  },
  pattern: {
    type: String,
    default: undefined,
  },
});

// 支持使用v-model
defineEmits(["update:modelValue"]);

const localValue = computed({
  get() {
    if (props.modelValue) {
      return props.modelValue;
    }
    return props.value;
  },
  set(val) {
    emit("update:modelValue", val);
  },
});

function getClasses(size, success, error) {
  let sizeValue, isValidValue;

  sizeValue = size && `form-control-${size}`;

  if (error) {
    isValidValue = "is-invalid";
  } else if (success) {
    isValidValue = "is-valid";
  } else {
    isValidValue = "";
  }

  return `${sizeValue} ${isValidValue}`;
}
</script>
<template>
  <div class="input-group">
    <label v-if="label" :class="label.class">{{
      typeof label == "string" ? label : label.text
    }}</label>
    <span v-if="icon" class="input-group-text"><i class="fas" :class="`fa-${icon}`" aria-hidden="true"></i></span>
    <input :id="id" :type="type" class="form-control" :class="[getClasses(size, success, error), inputClass]"
      :value="localValue" @input="$emit('update:modelValue', $event.target.value)" :placeholder="placeholder"
      :required="isRequired" :disabled="isDisabled" :pattern="pattern" />
  </div>
</template>
