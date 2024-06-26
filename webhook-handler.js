export default {
  async fetch(request) {
    if (request.method === 'POST') {
      const data = await request.json();
      // Procesar los datos del webhook aquí
      console.log('Webhook received:', data);

      return new Response('Webhook received', { status: 200 });
    } else {
      return new Response('Method Not Allowed', { status: 405 });
    }
  }
}