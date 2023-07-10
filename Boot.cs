using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.UI;

public class Boot : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void JavaInstaller()
    {
        System.Diagnostics.Process.Start(@"Launcher.exe");
    }

    public void JavaLauncher()
    {
        System.Diagnostics.Process.Start(@"MultiMC.exe");
    }

    public void BedrockInstaller()
    {
        System.Diagnostics.Process.Start(@"BedrockInstaller.exe");
    }

    public void BedrockLauncher()
    {
        System.Diagnostics.Process.Start(@"StartBedrockLauncher.exe");
    }

    public void AutoUpdate()
    {
        System.Diagnostics.Process.Start(@"autoupdate.exe");
    }

    public void OldJavaLauncher()
    {
        System.Diagnostics.Process.Start(@"betacraft-launcher-1.09_16.exe");
    }
}
