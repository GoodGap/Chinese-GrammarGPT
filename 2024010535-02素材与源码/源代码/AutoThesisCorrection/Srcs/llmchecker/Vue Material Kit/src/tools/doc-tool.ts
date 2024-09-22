import mammoth from "mammoth";
export async function convertDocxToHTML(file: File): Promise<string> {
  return mammoth.convertToHtml({ arrayBuffer: await file.arrayBuffer() }).then((result) => result.value);
}