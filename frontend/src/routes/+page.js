// /src/routes/+page.js
import { redirect } from "@sveltejs/kit";

export function load() {
  throw redirect(307, "/home"); // Redirect / to /home
}
