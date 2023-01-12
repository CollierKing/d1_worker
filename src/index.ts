export interface Env {
    d1_test_binding: D1Database;
}

export default {
    async fetch(request: Request, env: Env) {
        const {pathname} = new URL(request.url);

        const formData = await request.formData();
        const sql:string = formData.get('sql');
        console.log("sql", sql)

        if (pathname === "/api/beverages") {
            const {results} =
                await env.d1_test_binding
                    .prepare("SELECT * FROM Customers WHERE CompanyName = ?")
                    .bind("Bs Beverages")
                    .all();

            return Response.json(results);

        } else if (pathname == "/api/query") {

            // console.log("Done")
            // return Response.json({"sql":sql});

            // if (typeof sql === "string") {
            const {results} =
                await env.d1_test_binding
                    .prepare(sql)
                    .all();
            // }

            return Response.json(results);
        }
        return new Response("Call /api/beverages to see everyone who works at Bs Beverages");
    },
};
