const puppeteer = require("puppeteer");
const path = require("path");
const fs = require("fs");

// Cria a pasta de screenshots, se não existir
const screenshotDir = path.join(__dirname, "screenshots");
if (!fs.existsSync(screenshotDir)) {
  fs.mkdirSync(screenshotDir);
}

async function telaDeLoginUserNaoCadastrado() {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  try {
    await page.goto("http://localhost:3000/", {
      waitUntil: "networkidle2",
    });

    const screenshotPath = path.join(screenshotDir, "pagina_inicial.png");
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`✅ Screenshot salvo em: ${screenshotPath}`);
  } catch (error) {
    console.error("Erro ao acessar a página inicial:", error);
  }
}

async function FormPrenchidoErros() {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  try {
    await page.goto("http://localhost:3000/criar-usuario", {
      waitUntil: "networkidle2",
    });

    await page.waitForSelector(".p-dropdown");
    await page.click(".p-dropdown");

    await page.waitForSelector(".p-dropdown-panel");

    await page.evaluate(() => {
      const items = Array.from(document.querySelectorAll("li.p-dropdown-item"));
      const targetItem = items.find(
        (item) => item.textContent.trim() === "Maestro"
      );
      if (targetItem) {
        targetItem.click();
      }
    });

    await page.waitForSelector('input[name="cpf"]');
    await page.type('input[name="cpf"]', "123.456.789-40");

    await page.type('input[name="nome"]', "");
    await page.type('input[name="email"]', "joaoomaestr");
    await page.type('input[name="senha"]', "senha123");
    await page.type('input[name="confirmação"]', "senha1323");
    await page.type(
      'input[name="questão"]',
      "Qual o nome do seu primeiro pet?"
    );
    await page.type('input[name="resposta"]', "Rex");

    await new Promise((resolve) => setTimeout(resolve, 1000));
    await page.evaluate(() => {
      const buttons = Array.from(document.querySelectorAll("button"));
      const salvarButton = buttons.find((btn) =>
        btn.textContent.includes("Salvar")
      );
      if (salvarButton) {
        salvarButton.click();
      }
    });
    await new Promise((resolve) => setTimeout(resolve, 2000));

    const screenshotPath = path.join(
      screenshotDir,
      "formulario_enviado_erros.png"
    );
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`✅ Screenshot salvo em: ${screenshotPath}`);
  } catch (error) {
    console.error("Erro ao preencher e enviar o formulário:", error);
  } finally {
    await browser.close();
  }
}

async function FormPreenchidoCorretamente() {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  try {
    await page.goto("http://localhost:3000/criar-usuario", {
      waitUntil: "networkidle2",
    });

    await page.waitForSelector(".p-dropdown");
    await page.click(".p-dropdown");

    await page.waitForSelector(".p-dropdown-panel");

    await page.evaluate(() => {
      const items = Array.from(document.querySelectorAll("li.p-dropdown-item"));
      const targetItem = items.find(
        (item) => item.textContent.trim() === "Maestro"
      );
      if (targetItem) {
        targetItem.click();
      }
    });

    await page.waitForSelector('input[name="cpf"]');
    await page.type('input[name="cpf"]', "123.456.789-40");

    await page.type('input[name="nome"]', "Jõao Arrocha");
    await page.type('input[name="email"]', "joaoomaestro@gmail.com");
    await page.type('input[name="senha"]', "senha123");
    await page.type('input[name="confirmação"]', "senha123");
    await page.type(
      'input[name="questão"]',
      "Qual o nome do seu primeiro pet?"
    );
    await page.type('input[name="resposta"]', "Rex");

    await new Promise((resolve) => setTimeout(resolve, 1000));

    const screenshotPath = path.join(
      screenshotDir,
      "form_preenchido_corretamente.png"
    );
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`✅ Screenshot salvo em: ${screenshotPath}`);

    await showConferirDados(page);
  } catch (error) {
    console.error("Erro ao preencher e enviar o formulário:", error);
  } finally {
    await browser.close();
  }
}

async function showConferirDados(page) {
  // Desabilita animações/transições para capturar o estado final do modal
  // await page.addStyleTag({
  //   content: `* { transition: none !important; animation: none !important; }`,
  // });

  // Clica no botão "Salvar" para abrir o modal de confirmação
  await page.evaluate(() => {
    const buttons = Array.from(document.querySelectorAll("button"));
    const salvarButton = buttons.find((btn) =>
      btn.textContent.includes("Salvar")
    );
    if (salvarButton) {
      salvarButton.click();
    }
  });

  // Aguarda que o modal esteja visível
  await page.waitForSelector(".p-dialog.p-component", { visible: true });

  // Aguarda até que o modal esteja centralizado na tela
  // await page.waitForFunction(() => {
  //   const modal = document.querySelector(".p-dialog.p-component");
  //   if (!modal) return false;
  //   const rect = modal.getBoundingClientRect();
  //   return (
  //     Math.abs(rect.left + rect.width / 2 - window.innerWidth / 2) < 5 &&
  //     Math.abs(rect.top + rect.height / 2 - window.innerHeight / 2) < 5
  //   );
  // });

  // Aguarda que o backdrop esteja totalmente visível (ajuste a classe se necessário)
  // await page
  //   .waitForSelector(".p-dialog-mask", { visible: true })
  //   .catch(() => {});
  await new Promise((resolve) => setTimeout(resolve, 1000));

  await page.evaluate(() => {
    document.body.style.zoom = "0.65";
  });
  await new Promise((resolve) => setTimeout(resolve, 1000));

  // Opcional: rolar para o topo para garantir a visualização completa
  // await page.evaluate(() => window.scrollTo(0, 0));

  // Tira o screenshot do modal com o backdrop e centralizado
  const screenshotPath = path.join(screenshotDir, "conferir.png");
  await page.screenshot({ path: screenshotPath, fullPage: true });
  console.log(`✅ Screenshot salvo em: ${screenshotPath}`);
}

const executarTestes = async () => {
  // await telaDeLoginUserNaoCadastrado();
  // await FormPrenchidoErros();
  await FormPreenchidoCorretamente();
};

executarTestes();
