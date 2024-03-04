import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const usePageInfoStore = defineStore("pageinfo", () => {
    let pageNameHint = '';

	return { pageNameHint };
});
