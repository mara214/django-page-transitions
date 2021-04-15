import commonjs from '@rollup/plugin-commonjs';
import postcss from 'rollup-plugin-postcss';
import resolve from '@rollup/plugin-node-resolve';
import typescript from '@rollup/plugin-typescript';
import { terser } from 'rollup-plugin-terser';


const production = !process.env.ROLLUP_WATCH;

export default [
	{
		input: 'client/js/main.ts',
		output: {
			file: 'static/js/main.js',
			format: 'iife',
			sourcemap: true
		},
		plugins: [
			resolve(),
			commonjs(),
			typescript(),
			production && terser()
		]
	},
	{
		input: 'client/css/main.css',
		output: {
			dir: 'static/css',
			exports: 'auto',
			format: 'cjs'
		},
		plugins: [
			postcss({
				config: {
					path: "./postcss.config.js",
				},
				extensions: [".css"],
				extract: 'main.css',
				minimize: production
			})
		]
	}
];
