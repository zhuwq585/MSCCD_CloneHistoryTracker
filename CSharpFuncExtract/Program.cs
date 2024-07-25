using System;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.IO;
using System.Linq;
using System.Text.Json; // 引入JSON处理库

class Program
{
    static void Main(string[] args)
    {


        if (args.Length == 0)
        {
            // Console.WriteLine("Usage: CSharpCodeAnalysis <path_to_csharp_file>");
            return;
        }

        string codeFilePath = args[0];
        if (!File.Exists(codeFilePath))
        {
            // Console.WriteLine($"File not found: {codeFilePath}");
            return;
        }

        // 替换为你的C#文件路径
        // string codeFilePath = @"/Users/syu/IoT_Projs/C#/QuickbirdUWPDashboard/Quickbird/ViewModels/SettingsViewModel.cs";
        string code = File.ReadAllText(codeFilePath);

        SyntaxTree tree = CSharpSyntaxTree.ParseText(code);
        var root = (CompilationUnitSyntax)tree.GetRoot();

        var methodDeclarations = root.DescendantNodes().OfType<MethodDeclarationSyntax>();

        foreach (var method in methodDeclarations)
        {
            var lineNumber = tree.GetLineSpan(method.Span).StartLinePosition.Line + 1; // 行号是从0开始的，所以加1
            var endLineNumner = tree.GetLineSpan(method.Span).EndLinePosition.Line + 1;
            var methodName = method.Identifier.ValueText;
            var parameters = string.Join(", ", method.ParameterList.Parameters.Select(p => p.ToFullString()));

            var methodInfo = new
            {
                name = methodName,
                startLine = lineNumber,
                endLine = endLineNumner,
                paramss = method.ParameterList.Parameters.Select(p => new { type = p.Type.ToString(), name = p.Identifier.ValueText }).ToList()
                // paramss = parameters
            };


            string json = JsonSerializer.Serialize(methodInfo, new JsonSerializerOptions { WriteIndented = false });
            Console.WriteLine(json);

            // Console.WriteLine($"Method: {methodName}, Line: {lineNumber},Endline: {endLineNumner}, Parameters: {parameters}");
        }
    }
}
