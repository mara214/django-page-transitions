import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';


const production = !process.env.ROLLUP_WATCH;

export default {
	input: 'client/js/main.js',
	output: {
		file: 'static/js/main.js',
		format: 'iife',
		sourcemap: true
	},
	plugins: [
		resolve(),
		commonjs(),
		production && terser()
	]
};
