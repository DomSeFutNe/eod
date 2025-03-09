import js from "@eslint/js";
import globals from "globals";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";
import prettierPlugin from "eslint-plugin-prettier";
import * as importPlugin from "eslint-plugin-import";

export default [
  {
    ignores: ["dist"],
  },
  {
    files: ["src/**/*.{ts,tsx}"],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parser: tsParser,
      parserOptions: {
        sourceType: "module",
        project: "./tsconfig.app.json",
      },
    },
    plugins: {
      "@typescript-eslint": tseslint,
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
      prettier: prettierPlugin,
      import: importPlugin,
    },
    rules: {
      // React Rules
      "react-refresh/only-export-components": [
        "warn",
        { allowConstantExport: true },
      ],
      ...reactHooks.configs.recommended.rules,

      // Prettier Rules
      "prettier/prettier": "error",

      // Import Sorting
      "import/order": [
        "warn",
        {
          groups: [
            "builtin",
            "external",
            "internal",
            "parent",
            "sibling",
            "index",
            "object",
            "type",
          ],
          "newlines-between": "always",
          "alphabetize": { order: "asc", caseInsensitive: true },
        },
      ],
    },
  },
];
