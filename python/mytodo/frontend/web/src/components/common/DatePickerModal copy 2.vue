<template>
	<div class="text-center">
		<v-dialog v-model="dialog" width="500">
			<template v-slot:activator="{ on }">
				<v-btn color="red lighten-2" dark v-on="on">
					Click Me
				</v-btn>
			</template>

			<v-row justify="center">
				<v-date-picker
					v-model="picker"
					show-current="current"
				></v-date-picker>
			</v-row>
		</v-dialog>
	</div>
</template>
<script>
export default {
	data() {
		return {
			current: new Date().toISOString().substr(0, 10),
			picker: new Date().toISOString().substr(0, 10),
			dialog: false
		};
	}
};
</script>
