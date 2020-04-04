<template>
	<v-menu
		ref="menu1"
		v-model="menu1"
		:close-on-content-click="false"
		transition="scale-transition"
		offset-y
		max-width="290px"
		min-width="290px"
	>
		<template v-slot:activator="{ on }">
			<v-text-field
				v-model="dateFormatted"
				label="Date"
				hint="MM/DD/YYYY format"
				persistent-hint
				prepend-icon="mdi-calendar"
				@blur="onBlur"
				v-on="on"
			></v-text-field>
		</template>
		<v-date-picker
			v-model="date"
			no-title
			@input="menu1 = false"
		></v-date-picker>
	</v-menu>
</template>
<script>
export default {
	props: {
		onSetDate: Function
	},
	data: vm => ({
		date: new Date().toISOString().substr(0, 10),
		dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
		menu1: false,
		dialog: false
	}),

	watch: {
		date() {
			this.dateFormatted = this.formatDate(this.date);
			this.onSetDate(this.dateFormatted);
		}
	},

	methods: {
		formatDate(date) {
			if (!date) return null;

			const [year, month, day] = date.split("-");
			return `${month}/${day}/${year}`;
		},
		parseDate(date) {
			if (!date) return null;

			const [month, day, year] = date.split("/");
			return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
		},
		onBlur: function() {
			this.date = this.parseDate(this.dateFormatted);
		}
	}
};
</script>
